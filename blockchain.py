from hashmap import HashMap

class Transaction():
    def __init__(self, from_user, to_user, amount):
        self.from_user = from_user
        self.to_user = to_user
        self.amount = amount
    
    def __hash__(self):
        return hash((self.from_user, self.to_user, self.amount))
    
    def __eq__(self, other_transaction):
        from_user = self.from_user == other_transaction.from_user
        to_user = self.to_user == other_transaction.to_user
        amount = self.amount == other_transaction.amount

        return from_user and to_user and amount
    
    def __lt__(self, other):
        from_user_lt = self.from_user < other.from_user
        to_user_lt = self.to_user < other.to_user
        amount_lt = self.amount < other.amount

        return from_user_lt or to_user_lt or amount_lt
    
    def __str__(self):
        return f"from: {self.from_user}, to: {self.to_user}, amount: {self.amount}"

class Block():
    def __init__(self, transactions=None, previous_block_hash=None):
        if transactions is not None and isinstance(transactions, tuple):
            self.transactions = transactions
        else:
            self.transactions = ()

        self.previous_block_hash = previous_block_hash

    def add_transaction(self, transaction):
        new_transaction_tuple = (*self.transactions, transaction)
        self.transactions = new_transaction_tuple

    def __hash__(self):
        return hash((self.transactions, self.previous_block_hash))
    
    def __str__(self):
        out = "#"*40 + "\n"
        for trans in self.transactions:
            out += (str(trans) + "\n")
        out += "#"*40 + "\n"

        return out

class Ledger():
    def __init__(self):
        self._hashmap = HashMap() # user -> funds
    
    def has_funds(self, user, amount):
        if user not in self._hashmap:
            return False
        balance = self._hashmap.get(user)
        return balance >= amount
    
    def __contains__(self, user):
        return user in self._hashmap

    def deposit(self, user, amount):
        balance = 0
        if user in self:
            balance = self._hashmap.get(user)

        new_balance = balance + amount
        self._hashmap.set(user, new_balance)
    
    def transfer(self, user, amount):
        if user not in self:
            raise ValueError(f"User {user} does not exist and therefore is not elligible for transfers")

        balance = self._hashmap.get(user)
        new_balance = balance - amount

        if new_balance < 0:
            raise ValueError(f"User: {user} has insuffient balance: {balance} for transaction amount: {amount}")

        self._hashmap.set(user, new_balance)

    def __str__(self):
        return str(self._hashmap._map)

class Blockchain():
    '''Contains the chain of blocks.'''

    #########################
    # Do not use these three values in any code that you write. 
    _ROOT_BC_USER = "ROOT"            # Name of root user account.  
    _BLOCK_REWARD = 1000              # Amoung of HuskyCoin given as a reward for mining a block
    _TOTAL_AVAILABLE_TOKENS = 999999  # Total balance of HuskyCoin that the ROOT user receives in block0
    #########################

    def __init__(self):
        self._blockchain = list()     # Use the Python List for the chain of blocks
        self._bc_ledger = Ledger()    # The ledger of HuskyCoin balances
        # Create the initial block0 of the blockchain, also called the "genesis block"
        self._create_genesis_block()

    # This method is complete. No additional code needed.
    def _create_genesis_block(self):
        '''Creates the initial block in the chain.
        This is NOT how a blockchain usually works, but it is a simple way to give the
        Root user HuskyCoin that can be subsequently given to other users'''
        trans0 = Transaction(self._ROOT_BC_USER, self._ROOT_BC_USER, self._TOTAL_AVAILABLE_TOKENS)
        block0 = Block([trans0])
        self._blockchain.append(block0)
        self._bc_ledger.deposit(self._ROOT_BC_USER, self._TOTAL_AVAILABLE_TOKENS)

    # This method is complete. No additional code needed.
    def distribute_mining_reward(self, user):
        '''
        You need to give HuskyCoin to some of your users before you can transfer HuskyCoing
        between users. Use this method to give your users an initial balance of HuskyCoin.
        (In the Bitcoin network, users compete to solve a meaningless mathmatical puzzle.
        Solving the puzzle takes a tremendious amount of copmputing power and consuming a lot
        of energy. The first node to solve the puzzle is given a certain amount of Bitcoin.)
        In this assigment, you do not need to understand "mining." Just use this method to 
        provide initial balances to one or more users.'''
        trans = Transaction(self._ROOT_BC_USER, user, self._BLOCK_REWARD)
        block = Block((trans,))
        self.add_block(block)


    def get_net_transfers(self, block : Block):
        net_transfer_map = HashMap()
        
        
        # Iterate through all transactions in block to tally net change in accounts
        for transaction in block.transactions:
            # Add change in `to_user`
            if transaction.to_user not in net_transfer_map:
                net_transfer_map.set(transaction.to_user, transaction.amount)
            elif transaction.to_user in net_transfer_map:
                balance = net_transfer_map.get(transaction.to_user) + transaction.amount
                net_transfer_map.set(transaction.to_user, balance)
            
            # Add change in `from_user`
            if transaction.from_user not in net_transfer_map:
                net_transfer_map.set(transaction.from_user, -transaction.amount)
            elif transaction.from_user in net_transfer_map:
                balance = net_transfer_map.get(transaction.from_user) - transaction.amount
                net_transfer_map.set(transaction.from_user, balance)

        return net_transfer_map

    def _validate_block_transactions(self, net_transfer_map):
        """
        Validates that all users have the finances to make each transaction

        Uses a map of: user -> net change
        """

        # Validate that each user has enough funds for their net activies in the block
        for user, change in net_transfer_map.items():
            if change < 0: # If change is negative, the user is net spending
                if not self._bc_ledger.has_funds(user, abs(change)):
                    return False
        
        return True
    
    
    def validate_chain(self):
        previous_hash = None
        for block in self._blockchain:
            if block.previous_block_hash != previous_hash:
                return False
            previous_hash = hash(block)

        return True
        



    def add_block(self, block : Block):
        net_transfers = self.get_net_transfers(block)

        if not self._validate_block_transactions(net_transfers):
            return False
        
        previous_block = self._blockchain[-1]

        block.previous_block_hash = hash(previous_block)

        for user, change in net_transfers.items():
            self._bc_ledger.deposit(user, change)

        self._blockchain.append(block)

        return True

                
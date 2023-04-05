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

    
class Block():
    def __init__(self, transactions=None, previous_block_hash=0):
        if transactions is not None and isinstance(transactions, tuple):
            self.transactions = transactions
        else:
            self.transactions = ()

        self.previous_block_hash = previous_block_hash

    def __hash__(self):
        return hash((self.transactions, self.previous_block_hash))
    
    def __eq__(self, otb):
        hash_same = self.previous_block_hash == otb.previous_block_hash
        transactions_same = self.transactions == otb.transactions

        return hash_same and transactions_same


class Ledger():
    def __init__(self):
        pass
    
    # def has_funds(self, user, amount):
    #     if user not in self._hashmap:
    #         return False
    #     balance = self._hashmap.get(user)
    #     return balance >= amount

    def deposit(self, user, amount):
        pass

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
        block = Block([trans])
        self.add_block(block)

    # TODO - add the rest of the code for the class here

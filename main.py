from Block import Block

blockchain = []

genesis_block = Block("Chancellor on the brink...", ['_____ sent 1 BTC to _____'])

print(genesis_block.block_hash)

second_block = Block(genesis_block.block_hash, ['_____ sent 1 BTC to _____'])

print(second_block.block_hash)
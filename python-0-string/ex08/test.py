from time import sleep
from tqdm import tqdm  # This is the original tqdm
from Loading import ft_tqdm  # This is your custom implementation

# Test ft_tqdm (your function)
for elem in ft_tqdm(range(333)):
    sleep(0.005)
print()

# Test original tqdm
for elem in tqdm(range(333)):
    sleep(0.005)
print()

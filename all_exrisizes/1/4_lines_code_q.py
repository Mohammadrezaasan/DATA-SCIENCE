from tabulate import tabulate
text = list(input('Enter your text: ').replace(' ', ''))
result = list(set([(x, str(text.count(x))) for x in text]))
print(tabulate(result, headers=["NAME", "FREQUENCY"], tablefmt="grid"))
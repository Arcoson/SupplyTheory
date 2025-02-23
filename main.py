from colorama import Fore, Style, init
import json

init(autoreset=True)

def print_colored(text, color=Fore.WHITE):
    print(color + text)

print_colored("Welcome to SupplyTheory v3.1", Fore.GREEN)
print_colored("Type .help to view all commands.", Fore.YELLOW)

data = {
    "chains": {},
    "biomes": {}
}

def save_data():
    with open('data.json', 'w') as f:
        json.dump(data, f)

def load_data():
    global data
    try:
        with open('data.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        pass

load_data()

while True:
    initcmd = input(Fore.CYAN + "$: ").strip()

    if initcmd == '.help':
        print_colored("Commands:", Fore.YELLOW)
        print_colored('.chain - Create a Chain', Fore.WHITE)
        print_colored('{chain}.pro - Create a Product', Fore.WHITE)
        print_colored('{chain}.pro.info - Add Product Details', Fore.WHITE)
        print_colored('{chain}.pro.del - Delete a Product', Fore.WHITE)
        print_colored('{chain}.find - Find a Product', Fore.WHITE)
        print_colored('{chain}.export - Export a Chain', Fore.WHITE)
        print_colored('.import - Import a Chain', Fore.WHITE)
        print_colored('.import.read - Read Imported Data', Fore.WHITE)
        print_colored('.display - List All Products', Fore.WHITE)
        print_colored('.len - Count Products', Fore.WHITE)
        print_colored('.biome - Create a Biome', Fore.WHITE)
        print_colored('.biome.export - Export a Biome', Fore.WHITE)
        print_colored('.biome.import - Import a Biome', Fore.WHITE)
        print_colored('{chain}.mul.pro - Create Multiple Products', Fore.WHITE)
        print_colored('.break - Exit', Fore.WHITE)

    elif initcmd == '.chain':
        chain_name = input(Fore.CYAN + "Name of Chain: ").strip()
        if chain_name not in data["chains"]:
            data["chains"][chain_name] = {"products": [], "types": [], "destinations": [], "info": []}
            print_colored(f"Chain {chain_name} has been generated.", Fore.GREEN)
            save_data()
        else:
            print_colored("Chain already exists.", Fore.RED)

    elif initcmd.endswith('.pro'):
        chain = initcmd.split('.')[0]
        if chain in data["chains"]:
            product_name = input(Fore.CYAN + "What is the name of the product: ").strip()
            product_type = input(Fore.CYAN + "What is the shipping type of product: ").strip()
            destination = input(Fore.CYAN + "What is the final place of product: ").strip()
            data["chains"][chain]["products"].append(product_name)
            data["chains"][chain]["types"].append(product_type)
            data["chains"][chain]["destinations"].append(destination)
            data["chains"][chain]["info"].append("")
            print_colored(f"Product {product_name} is created.", Fore.GREEN)
            save_data()
        else:
            print_colored("Chain not found.", Fore.RED)

    elif initcmd.endswith('.pro.info'):
        chain = initcmd.split('.')[0]
        if chain in data["chains"]:
            product_name = input(Fore.CYAN + "What is the name of the product: ").strip()
            if product_name in data["chains"][chain]["products"]:
                idx = data["chains"][chain]["products"].index(product_name)
                info = input(Fore.CYAN + "What is some info of the product: ").strip()
                data["chains"][chain]["info"][idx] = info
                print_colored(f"Info for {product_name} is updated.", Fore.GREEN)
                save_data()
            else:
                print_colored("Product not found.", Fore.RED)
        else:
            print_colored("Chain not found.", Fore.RED)

    elif initcmd.endswith('.pro.del'):
        chain = initcmd.split('.')[0]
        if chain in data["chains"]:
            product_name = input(Fore.CYAN + "What is the name of the product: ").strip()
            if product_name in data["chains"][chain]["products"]:
                idx = data["chains"][chain]["products"].index(product_name)
                data["chains"][chain]["products"].pop(idx)
                data["chains"][chain]["types"].pop(idx)
                data["chains"][chain]["destinations"].pop(idx)
                data["chains"][chain]["info"].pop(idx)
                print_colored(f"Product {product_name} is deleted.", Fore.GREEN)
                save_data()
            else:
                print_colored("Product not found.", Fore.RED)
        else:
            print_colored("Chain not found.", Fore.RED)

    elif initcmd.endswith('.find'):
        chain = initcmd.split('.')[0]
        if chain in data["chains"]:
            product_name = input(Fore.CYAN + "What is the name of the product: ").strip()
            if product_name in data["chains"][chain]["products"]:
                idx = data["chains"][chain]["products"].index(product_name)
                print_colored(f"Product {product_name} is found.", Fore.GREEN)
                print_colored(f"Type: {data['chains'][chain]['types'][idx]}", Fore.WHITE)
                print_colored(f"Destination: {data['chains'][chain]['destinations'][idx]}", Fore.WHITE)
                print_colored(f"Info: {data['chains'][chain]['info'][idx]}", Fore.WHITE)
            else:
                print_colored("Product not found.", Fore.RED)
        else:
            print_colored("Chain not found.", Fore.RED)

    elif initcmd.endswith('.export'):
        chain = initcmd.split('.')[0]
        if chain in data["chains"]:
            with open(f"{chain}_export.json", 'w') as f:
                json.dump(data["chains"][chain], f)
            print_colored(f"Chain {chain} exported successfully.", Fore.GREEN)
        else:
            print_colored("Chain not found.", Fore.RED)

    elif initcmd == '.import':
        try:
            chain_name = input(Fore.CYAN + "Enter the name of the chain to import: ").strip()
            with open(f"{chain_name}_export.json", 'r') as f:
                imported_data = json.load(f)
                data["chains"][chain_name] = imported_data
            print_colored(f"Chain {chain_name} imported successfully.", Fore.GREEN)
            save_data()
        except FileNotFoundError:
            print_colored("No exported data file found.", Fore.RED)

    elif initcmd == '.display':
        for chain, details in data["chains"].items():
            print_colored(f"Chain: {chain}", Fore.YELLOW)
            for i, product in enumerate(details["products"]):
                print_colored(f"  Product: {product}", Fore.WHITE)
                print_colored(f"    Type: {details['types'][i]}", Fore.WHITE)
                print_colored(f"    Destination: {details['destinations'][i]}", Fore.WHITE)
                print_colored(f"    Info: {details['info'][i]}", Fore.WHITE)

    elif initcmd == '.len':
        total_products = sum(len(details["products"]) for details in data["chains"].values())
        print_colored(f"Total number of products: {total_products}", Fore.GREEN)

    elif initcmd == '.biome':
        biome_name = input(Fore.CYAN + "Biome Name: ").strip()
        biome_type = input(Fore.CYAN + "Biome Type: ").strip()
        product_link = input(Fore.CYAN + "What Product To Link: ").strip()
        found = False
        for chain, details in data["chains"].items():
            if product_link in details["products"]:
                data["biomes"][biome_name] = {"type": biome_type, "product": product_link}
                print_colored(f"Biome {biome_name} created and linked to {product_link}.", Fore.GREEN)
                save_data()
                found = True
                break
        if not found:
            print_colored("Product not found.", Fore.RED)

    elif initcmd == '.biome.export':
        biome_name = input(Fore.CYAN + "Enter the name of the biome to export: ").strip()
        if biome_name in data["biomes"]:
            with open(f"{biome_name}_biome_export.json", 'w') as f:
                json.dump(data["biomes"][biome_name], f)
            print_colored(f"Biome {biome_name} exported successfully.", Fore.GREEN)
        else:
            print_colored("Biome not found.", Fore.RED)

    elif initcmd == '.biome.import':
        try:
            biome_name = input(Fore.CYAN + "Enter the name of the biome to import: ").strip()
            with open(f"{biome_name}_biome_export.json", 'r') as f:
                imported_biome = json.load(f)
                data["biomes"][biome_name] = imported_biome
            print_colored(f"Biome {biome_name} imported successfully.", Fore.GREEN)
            save_data()
        except FileNotFoundError:
            print_colored("No exported biome file found.", Fore.RED)

    elif initcmd.endswith('.mul.pro'):
        chain = initcmd.split('.')[0]
        if chain in data["chains"]:
            num_products = int(input(Fore.CYAN + "How many products: "))
            for _ in range(num_products):
                product_name = input(Fore.CYAN + "What is the name of the product: ").strip()
                product_type = input(Fore.CYAN + "What is the shipping type of products: ").strip()
                destination = input(Fore.CYAN + "What is the final place of products: ").strip()
                data["chains"][chain]["products"].append(product_name)
                data["chains"][chain]["types"].append(product_type)
                data["chains"][chain]["destinations"].append(destination)
                data["chains"][chain]["info"].append("")
                print_colored("Created.", Fore.GREEN)
            save_data()
        else:
            print_colored("Chain not found.", Fore.RED)

    elif initcmd == '.break':
        print_colored("Exiting...", Fore.RED)
        break

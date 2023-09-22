print("Welcome to SupplyTheory v2.0\nType .help to view all commands.")
initcmd = input("$: ")
chain = ''
while True:
    if initcmd == '.help':
        print("Commands:\n")
        print('Create a Chain: .chain')
        print('Create a Product: {chain}.pro')
        print('Create Product Details: {chain}.pro.info')
        print('Delete a Product: {chain}.pro.del | use pro')
        print('To find a product: {chain}.find | lists all products')
        print('To export a chain: {chain}.export')
        print('To import a chain: .import')
        print('To read a chain: .import.read')
        print('To list all products: .display')
        print('Find the number of products: .len')
        print('To create a biome: .biome | Preset for products')
        print('To export a biome: .biome.export')
        print('To import a biome: .biome.import')
        print('To create a product line: .{chain}.mul.pro | Create multiple products with same type and destination')
        print('Exit through the command: .break')
        initcmd = input("$: ")
    elif initcmd == '.chain':
        ask_chain = input("Name of Chain: ")
        chain = ask_chain.strip()
        chains = []
        products = []
        types = []
        destinations = []
        info = []
        chains.append(chain)
        print("Chain {} has been generated.".format(chain))
        initcmd = input("$: ")
    elif initcmd == '{}.pro'.format(chain):
        ask_product = input("What is the name of the product: ")
        products.append(ask_product.strip())
        ask_type_product = input("What is the shipping type of product: ")
        types.append(ask_type_product.strip())
        ask_destination = input("What is the final place of product: ")
        destinations.append(ask_destination.strip())
        print(f"Product {ask_product} is created.")
        initcmd = input("$: ")
    elif initcmd == '{}.pro.info'.format(chain):
        ask_product_info = input("What is some info of the product: ")
        info.append(ask_product_info.strip())
        print(f"Info {ask_product_info} is created.")
        initcmd = input("$: ")
    elif initcmd == f'{chain}.pro.del':
        ask_del_product = input("What is the name of the product: ")
        if ask_del_product in products:
            result_rmv = products.index(ask_del_product)
            types_rmv = types[result_rmv]
            destinations_rmv = destinations[result_rmv]
            infos_rmv = info[result_rmv]
            print(f"Product {ask_del_product} is deleted.")
            initcmd = input("$: ")
        else:
            print("Product not found.")
            initcmd = input("$: ")
            continue
    elif initcmd == f'{chain}.find':
        ask_find_product = input("What is the name of the product: ")
        if ask_find_product in products:
            result_find = products.index(ask_find_product)
            types_find = types[result_find]
            destinations_find = destinations[result_find]
            infos_find = info[result_find]
            print(f"Product {ask_find_product} is found.")
            print(f"Type: {types_find}")
            print(f"Destination: {destinations_find}")
            print(f"Info: {infos_find}")
            initcmd = input("$: ")
        else:
            print("Product not found.")
            initcmd = input("$: ")
            continue
    elif initcmd == f'{chain}.export':
        print('Exported Chain into a data file.')
        textfile = open(f"data.txt", "w")
        for element in products, types, destinations, info:
            textfile.write(str(element) + '\n')
        textfile.close()
        initcmd = input("$: ")
    elif initcmd == '.import':
        try:
            with open('data.txt', 'r') as filetype:
                file_read = filetype.read()
                print(file_read)
                ImportBool = True
                lines = filetype.readlines()
                initcmd = input("$: ")
        except FileNotFoundError:
            print("No exported data file found.")
            ImportBool = False
            initcmd = input("$: ")
            continue
    elif initcmd == '.import.read':
        if ImportBool == True:
            print(file_read)
            initcmd = input("$: ")
        elif ImportBool == False:
            print("No exported data file found.")
            initcmd = input("$: ")
            continue
        else:
            print("No exported data file found.")
            initcmd = input("$: ")
            continue
    elif initcmd == '.display':
        display_products = products[:10]
        display_types = types[:10]
        display_destinations = destinations[:10]
        display_info = info[:10]
        ask_display = int(input('Products, Types, Destinations, Info (1,2,3,4): '))
        if ask_display == 1:
            print(display_products)
            initcmd = input("$: ")
        elif ask_display == 2:
            print(display_types)
            initcmd = input("$: ")
        elif ask_display == 3:
            print(display_destinations)
            initcmd = input("$: ")
        elif ask_display == 4:
            print(display_info)
            initcmd = input("$: ")
        else:
            print("Not Found")
            initcmd = input("$: ")
            continue
    elif initcmd == '.len':
        try:
            print(len(products))
            initcmd = input("$: ")
        except:
            print("No products found.")
            initcmd = input("$: ")
            continue
    elif initcmd == '.biome':
        biomes = []
        ask_biome = input("Biome Name: ")
        ask_biome_type = input("Biome Type: ")
        ask_biome_product = input("What Product To Link: ")
        try:
            ask_biome_product_index = products.index(ask_biome_product)
        except NameError:
            print("No Products Found")
            initcmd = input("$: ")
            continue
        biomes.append(ask_biome)
        biome_dict = {}
        biome_dict[ask_biome_type] = products[ask_biome_product_index]
        biome_bool = True
        initcmd = input("$: ")
    elif initcmd == '.biome.export':
        textfile2 = open("biome.txt", "w")
        for element2 in biome_dict:
            textfile2.write(str(element2) + ' : ' + str(biome_dict[element2]) + '\n')
        textfile2.close()
        print('Done.')
        initcmd = input("$: ")
    elif initcmd == '.biome.import':
        try:
            with open('biome.txt', 'r') as filetype3:
                file_read3 = filetype3.read()
                print(file_read3)
                lines3 = filetype3.readlines()
                initcmd = input("$: ")
        except FileNotFoundError:
            print("No exported data file found.")
            initcmd = input("$: ")
            continue
    elif initcmd == f'{chain}.mul.pro':
        ask_mul_num_products = int(input("How many products: "))
        for x in range(ask_mul_num_products):
            mul_ask = input("What is the name of the product: ")
            ask_mul_type_product = input("What is the shipping type of products: ")
            ask_mul_destination = input("What is the final place of products: ")
            products.append(mul_ask.strip())
            types.append(ask_mul_type_product.strip())
            destinations.append(ask_mul_destination.strip())
            print("Created.")
        initcmd = input("$: ")
    elif initcmd == '.break':
        break

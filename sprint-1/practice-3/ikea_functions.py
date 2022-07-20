
def find_products(catalog, product_type):
    '''
    | Help on user-defined function find_products:
    |
    | This function takes inputs: 
    | - catalog - dictionary containing ikea catalog items
    | - product_type - string containing product types in catalog (first item in dict value)
    | 
    | This function returns:
    | - new_dict - a dictionary containing only catalog items that match the input product_type
    '''
    # empty list to fill with items 
    selected_keys = []
    selected_vals = []
    # loop through each key 
    for key in catalog:
    # for each key, find the values 
        val = catalog[key]
        # check if the item category is in the values
        # if it is, add it to our selection list
        if product_type in val[0]:
            selected_keys.append(key)
            selected_vals.append(val)
    # make new dict to return 
    new_dict = dict(zip(selected_keys, selected_vals))
    # return our list 
    return new_dict

def remove_designer(catalog, product_type, designer_to_exclude):
    '''
    | Help on user-defined function remove_designer:
    |
    | This function takes inputs: 
    | - catalog - dictionary containing ikea catalog items
    | - product_type - string containing product types in catalog (first item in dict value)
    | - designer_to_exclude - string containing name of designer we want to remove from selection 
    | 
    | This function returns:
    | - final_selection - a dictionary containing only catalog items that match the input product_type 
    | AND does NOT include designer_to_exclude
    '''
    # run find_products, nested function 
    selection = find_products(catalog, product_type)
    # exclude designer in selection
    refined_selection = {key: val for key, val in selection.items() if designer_to_exclude not in val}
    return refined_selection

def filter_pricepoint(input_selection, max_price):
    '''
    | Help on user-defined function filter_pricepoint:
    |
    | This function takes inputs: 
    | - input_selection - dictionary containing ikea catalog items. can be original catalog dictionary or
    | filtered `refined_selection` dict from find_products, remove_designer, or other. 
    | - max_price - int or float indicating max budget. funciton will keep everything < this value. 
    | 
    | This function returns:
    | - final_selection - a dictionary containing only catalog items that match the input product_type 
    | AND does NOT include designer_to_exclude
    '''
    # empty lists to fill with keys & vals we keep 
    final_selection_keys = []
    final_selection_vals = []
    # loop through keys, get vals 
    for key in list(input_selection.keys()):
        val = input_selection[key]
        # if within budget add keys & vals to list
        if val[1] < max_price:
            input_selection_keys.append(key)           
            input_selection_vals.append(val)
    # zip lists into a new dictionary 
    final_selection = dict(zip(final_selection_keys, final_selection_vals))
    return final_selection

def select_designer(catalog, product_type, designer_to_select):
    '''    
    | Help on user-defined function select_designer:
    |
    | This function takes inputs: 
    | - catalog - dictionary containing ikea catalog items
    | - product_type - string containing product types in catalog (first item in dict value)
    | - designer_to_select - string containing name of designer we want to keep (exclude every other designer)
    | 
    | This function returns:
    | - refined_selection - a dictionary containing only catalog items that match the input product_type 
    | AND is designed by designer_to_select
    '''
    selection = find_products(catalog, product_type)
    refined_selection = {key: val for key, val in selection.items() if designer_to_select in val}
    return refined_selection


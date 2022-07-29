
def find_products(ikea_df, item_category):
    '''
    | Help on user-defined function find_products:
    |
    | This function takes inputs: 
    | - ikea_df - dataframe containing ikea catalog items
    | - item_category - string containing product types in catalog 
    | 
    | This function returns:
    | - selected_category - a dataframe containing only catalog items that match the input product_type
    '''
    selected_category = ikea_df[(ikea_df['category'] == item_category)]
    return selected_category

def find_products_remove_designer(ikea_df, item_category, designer_to_exclude):
    '''
    | Help on user-defined function remove_designer:
    |
    | This function takes inputs: 
    | - ikea_df - dataframe containing ikea catalog items
    | - item_category - string containing product types in catalog 
    | - designer_to_exclude - string containing name of designer we want to remove from selection 
    | 
    | This function returns:
    | - selected_category - a dataframe containing only catalog items that match the input product_type
    | AND does NOT include designer_to_exclude
    '''
    # first get category
    selected_category = find_products(ikea_df, item_category)
    # then filter to remove designer
    refined_selection = selected_category[selected_category['designer'] != designer_to_exclude]
    return refined_selection

def filter_pricepoint(input_selection, min_price, max_price):
    '''
    | Help on user-defined function filter_pricepoint:
    |
    | This function takes inputs: 
    | - input_selection - dataframe containing ikea catalog items. can be original or filtered.
    | - min_price - int or float indicating min budget. function will keep everything <= this value. 
    | - max_price - int or float indicating max budget. function will keep everything > this value. 
    | 
    | This function returns:
    | - final_selection - a dataframe containing only catalog items within budget range 
    '''
    final_selection = input_selection[(input_selection['price'] <= max_price) & 
                                      (input_selection['price'] > min_price)]
    return final_selection

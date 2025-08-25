response = client.campaigns.list() # list campaigns
response = client.campaigns.get("campaign_id") # get campaign info
response = client.ecommerce.get_all_store_customers("store_id") # ecom customers
response = client.ecommerce.orders() # ecom orders
response = client.ecommerce.get_all_order_line_items("store_id", "order_id") # ecom order line items

# TODO: Investigate Lists/Audiences (contacts) section of API Docs. Also campaign reporting. Also segments?

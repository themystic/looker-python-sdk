from looker.client import LookerClient

# instantiate LookerClient
client = LookerClient('Mkz9GRYoIhyuJ898YG89Ig',
                      'v1+MNxMg1vdmljYbtBhEDFEQSlAUEZd4xWd',
                      'https://demo.looker.com')
# create a query object no filters
query1 = client.query('orders',
                      'thelook',
                      ['orders.count', 'users.count'],
    		      {})

# create a query object
query2 = client.query('orders',
                      'thelook',
                      ['orders.count', 'users.count'],
                      {'users.state': '-%New%',
                       'orders.created_date': '90 days'})

# create another query object
query3 = client.query('orders', 'thelook', 
                      ['orders.count'],
                      {'users.created_date': '90 days'})
query3.add_filters({'orders.created_date': '90 days'})

print query1.run()
print query2.run()
print query3.run()

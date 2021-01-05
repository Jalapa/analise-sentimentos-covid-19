#Import das biblios
import os
import csv
from twarc import Twarc

#Chaves usadas para a API
consumer_key='IMJh4kjQLGDzUaT9t1v0RXm5Y'
consumer_secret='cjt9d684CpvElXof1BxUMgSakNnFBVLDweQTSpGZolzzrnU8JE'
access_token='968521944944529408-oI5NcJVaZellwrsPjhsQkQPDeAZJzKf'
access_token_secret='hc7bTI65fG97smD3ZEB6iCjLrBzHBxn2Sp6TIaX8fZSJZ'

#Criacao do objeto para hidratar os dados
t = Twarc(consumer_key, consumer_secret, access_token, access_token_secret)

#Variaveris para armazenar os dados do dataset
tweet_id = []
total = []
contError = 0
contRetweet = 0
cont = 0
contNotUs = 0
contall = 0
errorid = 0

#Abre o arquivo definido
file_name = 'new_export_dataframe' 
extension = 'csv'
path_file_name = file_name + '.' + extension
with open(path_file_name, 'r') as csvfile:
  plots = csv.reader(csvfile, delimiter = ',')
  next(plots, None)
  for row in plots:
    contall += 1
    try:
      id = ("{:.0f}".format(float(row[0])))
    except:
      errorid += 1
    #Hidrata o tweet a partir de seu ID
    try:
      for tweet in t.hydrate([int(id)]):
        if (tweet['place']['country_code'] == 'US'):
          if (tweet['full_text'].find('RT', 0, 3) == -1):
            # total.append([tweet['created_at'], row[1]])
            cont = cont + 1
            with open('tweets.csv', 'a', newline='') as file:
              writer = csv.writer(file)  
              writer.writerow([tweet['created_at'], row[1]])   
          else:
            contRetweet = contRetweet + 1 
        else:
          contNotUs += 1
    except:
      contError = contError + 1
    print(contall, ' - US =', cont, ' - RT =', contRetweet,' - NotUS =', contNotUs,' - Error =' ,contError,' - ErrorID =' ,errorid,'\n')

print("Total Tweets   - ", cont)
print("Total Retweets - ", contRetweet)
print("Total Errors   - ", contError)
print("Total Not US   - ", contNotUs)
print("Cont all - ", contall)

#Arquivo de gravacao
with open('tweets.csv', 'a', newline='') as file:
  writer = csv.writer(file)
  
  writer.writerow(['contall', 'cont', 'contRetweet', 'contNotUs', 'contError'])  
  writer.writerow([contall, cont, contRetweet, contNotUs, contError])
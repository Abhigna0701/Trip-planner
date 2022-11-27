import webbrowser  
countries=["Australia","Japan","France","South Africa","Italy"]  
my_dict={"Australia":["Sydney","Melbourne","Canberra","Perth","Brisbane"],"Japan":["Tokyo","Kyoto","Yokohama","Hiroshima","Nagasaki"],"France":["Paris","Cannes","Lyon","Marseille","Lyon"],"South Africa":["Cape Town","Bloemfontein","Durban","East London","Johannesburg",],"Italy":["Rome","Venice","Florence","Pisa","Naples"]}   
print("***********************") 
print("*WELCOME TO TRIP PLANNER*") 
print("***********************\n")

name=input("Hello there! What is your name? ") 
print("\nOh hey, "+name+"! Nice to meet you!")  
print("\nOur services extend to various countries. Right now, we can offer you a quality time in one of the following:\n") 
i=1 
for c in my_dict.keys():     
    print(str(i)+". "+str(c))     
    i+=1 
print()  
country=int(input("So, which country are you interested in? Please type in the index number: ")) 
my_country=countries[country-1] 
print() 
print(my_country+" is an amazing choice indeed! In "+my_country+" we offer a tour in one of the following cities:\n") 
i=1 
for v in my_dict[my_country]:     
    print(str(i)+". "+str(v))     
    i+=1 
print() 
city=int(input("So tell us! Which city do you plan do go to? Enter its index number: ")) 
my_city=my_dict[my_country][city-1] 
print() 
print("So you want to go to "+my_city+"? That is an awesome choice!") 
info=input("Do you want to know more about "+my_city+"?(Y/N) ") 
if(info=='y' or info=='Y'):    
    url_city="https://en.wikipedia.org/wiki/"+my_city     
    webbrowser.open_new_tab(url_city)
elif(info=='n' or info=='N'):
    print("It seems you already know about "+my_city+"! Awesome") 
nop=int(input("\nSo, "+name+". You must be bringing along a few people atleast, right? To help us plan your trip better, please tell us how many people you're bringing with you: ")) 
if(nop==0):     
    print("\nOh! So it's more like a solo trip!") 
else:    
    print("\nOh so it's the "+str(nop+1)+" going together! All of you will have a great time together!")  
days=int(input("For how many days are you planning to stay in "+my_city+"?")) 
budget=int(input("\nHow much money in INR are you planning to carry? ")) 
if(country==1):
    factor=0.20
elif(country==2):     
    factor=1.63 
elif(country==3):    
    factor=0.012 
elif(country==4):   
    factor=0.18 
elif(country==5):
    factor=0.012
print() 
print(str(budget)+" INR is around "+str(int(budget*factor))+" in "+my_country+"'s native currency") 
if(budget<500000):
     print("\nThis much money is sufficient! You'll spend around "+str(int(budget*factor/days))+" per day on average.") 
else:
     print("\nThis much money is more than enough for you to enjoy this trip to the fullest!") 
hotelbooked=False 
print("\nNow let's see the Hotel's where you could be staying for the trip!") 
choice=input("Shall we? (Y/N)") 
def book_hotel(choice):     
    if(choice=='N' or choice=='n'): 
        print("\nOkay then we'll come back to this step later on!") 
    elif(choice=='y' or choice=='Y'):    
        urlh="https://www.trivago.in/?iSemThemeId=10982&iPathId=90137&sem_keyword=hotels%20in%20"+my_city+"&sem_creativeid=252826282041&sem_matchtype=e&sem_network=g&sem_device=c&sem_placement=&sem_target=&sem_adposition=1t2&sem_param1=&sem_param2=&sem_campaignid=211776628&sem_adgroupid=16839635428&sem_targetid=kwd-335473966&sem_location=9062209&cip=9112001021&gclid=CjwKCAjw2dvWBRBvEiwADllhn84r4QkRQeI4xlDGpFhgM8tlyn6d3ZQPICLRmWYj6kM0QDCKiR05kxoCX-UQAvD_BwE"         
        webbrowser.open_new_tab(urlh) 
        hotelbooked=True  
book_hotel(choice)  
print("\nNow let's go ahead and book the tickets.") 
flightbooked=False 
def book_flight():
    print("\nWhich of the following sites do you prefer?")     
    site=int(input("1.Clear Trip\n2.Goibibo\n3.Yatra.com\nChoice: "))     
    if(site==1):
        url="https://www.cleartrip.com/flights/international/results?from=BOM&to="+my_city+"&depart_date=29/12/2018&adults=1&childs=0&infants=0&class=Economy&airline=&carrier=&intl=y&sd=1524084890374&page=loaded"     
    elif(site==2):
        url="https://www.goibibo.com/flights/air-BOM-"+my_city+"-20180513-20180517-1-0-0-E-I/"     
    elif(site==3):
        url="https://www.yatra.com/international-flights/mumbai-to-"+my_city+"-flights"   
    info2=input("Proceed to webiste?(Y/N) ")    
    if(info2=='y' or info2=='Y'):
        webbrowser.open_new_tab(url)         
        book=input("\nDid you find your desired seat? (Y/N): ") 
        if(book=='n' or book=='N'): 
            book_flight()        
        else:             
            flight_booked=True             
        print("\nOkay that's great!")     
    else:         
        print("\nOkay we'll do that later!")  
book_flight()  
if(hotelbooked==False):
    choice=input("\nWould you like to book the Hotel Room now? (Y/N): ")     
    if(choice=='Y' or choice=='y'):
        print("\nOkay let's go!")
        book_hotel(choice)     
    else:
        print("Alright then!")    
if(flightbooked==False):
    choice=input("\nWould you like to book the Flight tickets now? (Y/N): ")     
    if(choice=='Y' or choice=='y'):
        print("\nOkay let's go!") 
        book_flight() 
print() 
print("We genuinely hope you have an amazing trip and return home with plenty of unforgettable moments! Hope you'll think of us next time when you wish to travel once again. See you later, "+name+"!")

rules = {
    None : "raining",
    "raining":"ground is wet",
    "ground is wet" : "ground is slipery",
    "ground is slipery" : None,

    None: "not raining",
    "not raining" : "the ground is dry",
    "the ground is dry" : "ground is not slipery",
    "ground is not slipery" : "can play cricket",
    "can play cricket" : None,

    None : "sunny",
    "sunny" : "the ground is dry"

    }

def forward_chaining():
    weather = int(input("what is happnig : \n1.raining \n2.Not Raining \n3.sunny \n-> "))
    fact = None
    goal = "can play cricket"

    if(weather == 1):
        fact  = "raining"
    elif(weather == 2):
        fact = "not raining"
    elif(weather == 3):
        fact = "sunny"

    
    output = list()
    statement = fact
    

    output.append(statement)
    while(statement != None):
        statement = rules[statement]
        output.append(statement)

        if(statement == goal):
            break


    if(statement == goal):
        print("----x Goal Reached x----")
    else:
        print("----x Goal cannot be Reached x----")
        
    for i in output:
                print(i,"->")




forward_chaining()
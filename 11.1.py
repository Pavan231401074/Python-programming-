    a=input()

    if(len(a)==0):

        print("Error: Please enter a valid age.")

    elif a.isnumeric():

        print("You are",a,"years old.")

    else:

        print("Error: Please enter a valid age.")

except:

    print("Error: Please enter a valid age.")

        num1 = float(input())

        num2 = float(input())

       

        division_result = num1 / num2

        modulo_result = num1 % num2

       

        print(division_result)

        

    except ValueError:

        print("Error: Non-numeric input provided.")

    except ZeroDivisionError:

        print("Error: Cannot divide or modulo by zero.")





if __name__ == "__main__":

    main()

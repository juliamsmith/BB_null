import sys # this is needed for command line arguments
import imp # this is to import modules from strings

def sum_three_numbers(a, b, c):
    print(a + b + c)
    return(a + b + c)

if __name__ == "__main__": # special line: code to execute when you call this program
    # import the parameter file
    myin = imp.load_source(name = "myin", pathname = sys.argv[1])
    x, y, z = (myin.x, myin.y, myin.z)
    print("My variables are", x, y, z)
    print("Their sum is", sum_three_numbers(x, y, z))


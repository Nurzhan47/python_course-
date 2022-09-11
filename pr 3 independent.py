
def isalive(health):
        return False if (health<0 and health!=0) else True
a=int(input())
print(isalive(a))

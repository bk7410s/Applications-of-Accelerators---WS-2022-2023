class particle:
    def __init__(data,z,a):
        data.z=z
        data.a=a
        data.n=data.a-data.z
    def __str__(data):
        return f"neutron number = {data.n}"
z=int(input("Enter the number of proton number = "))
a=int(input("Enter the number of mass number = "))        
answer=particle(z,a)
print(answer)

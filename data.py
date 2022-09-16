from faker import Faker

fake=Faker()

def get_reg_user():
    return{
        "name":fake.name(),
        "address":fake.address(),
        "created_At":fake.year()
    }

if __name__ =='__main__':
    print(get_reg_user())
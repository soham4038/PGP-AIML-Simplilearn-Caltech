from datetime import datetime, timedelta
class CarRental:
    '''Contains methods to display, rent and return cars. Also updates avaliable cars on renting or returning'''
    
    global avl_cars;
    global all_cars;
    all_cars={12:"Hyundai i20",22:"Honda City VX",23:"Kia Sonet",24:"Toyota Innova",
              25:"Toyota Innova 2018",26:"Ford GT",27:"BMW M3",29:"BMW i8",30:"RangeRover",
              31:"Nissan Magnite",32:"Suzuki",33:"LandRover",34:"Mahindra Scorpio",35:"Jeep"};
    avl_cars={12:"Hyundai i20",22:"Honda City VX",23:"Kia Sonet",24:"Toyota Innova",
              25:"Toyota Innova 2018",26:"Ford GT",27:"BMW M3",29:"BMW i8",30:"RangeRover",
              31:"Nissan Magnite",32:"Suzuki",33:"LandRover",34:"Mahindra Scorpio",35:"Jeep"};
    
    #Display Avaliable Cars
    def display(self):
        print("Car ID \t Model\n");
        for key, value in avl_cars.items():
            print(f"{key}:\t {value}")

    #Hourly Renting 
    '''Retuns selected cars, book time and rent'''
    
    def hourly():
        sel_cars={}
        num=int(input("Number of Cars"));
        if (num>len(avl_cars) or num<0):
            print("Cars not avaliable");
        else:
            print("Avaliable Cars:\n");
            CarRental.display(avl_cars)
            for i in range(num):
                ip=(int) (input("Enter car ID."))
                sel_cars[ip]=avl_cars.get(ip);
                avl_cars.pop(ip)     
            booktime=datetime.now();
            return (sel_cars,booktime,1,num)   
   
    #Daily Renting 
        
    def daily():
        sel_cars={}
        num=int(input("Number of Cars"));
        if (num>len(avl_cars) or num<0):
            print("Cars not avaliable");
        else:
            print("Avaliable Cars:\n");
            CarRental.display(avl_cars)
            for i in range(num):
                ip=(int) (input("Enter car ID."))
                sel_cars[ip]=avl_cars.get(ip);
                avl_cars.pop(ip)     
            booktime=datetime.now();
            return (sel_cars,booktime,2,num)      

    #Weekly Renting 
    def weekly():
        sel_cars={}
        num=int(input("Number of Cars"));
        if (num>len(avl_cars) or num<0):
            print("Cars not avaliable");
        else:
            print("Avaliable Cars:\n");
            CarRental.display(avl_cars)
            for i in range(num):
                ip=(int) (input("Enter car ID."))
                sel_cars[ip]=avl_cars.get(ip);
                avl_cars.pop(ip)     
            booktime=datetime.now();
            return (sel_cars,booktime,3,num)        

    #Return cars, update inventory and display rent

    def return_cars(booktime,mode,num,ret_cars):
        curr_time=datetime.now();
        rent=0;
        if (mode==1):
            secs= (curr_time-booktime).total_seconds();
            hrs=(int)(secs//60) +1
            rent= num*2.25*hrs;
        elif (mode==2):
            secs= (curr_time-booktime).total_seconds();
            days=(int)((secs//60)/24)+1;
            rent= num*2.00*days*22;
        else:
            secs= (curr_time-booktime).total_seconds();
            weeks=(int)(((secs//60)/24)/7)+1;
            rent =num*2.00*22*6*weeks;
        avl_cars.update(ret_cars);
        print("Total rent is ",rent)
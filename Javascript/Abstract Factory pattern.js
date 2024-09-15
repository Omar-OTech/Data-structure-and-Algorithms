function Car() {
    this.name = 'Car';
    this.wheels = 4;
}

function Truck() {
    this.name = 'Truck';
    this.wheels = 6;
}

function Bike() {
    this.name = 'Bike';
    this.wheels = 2;
}

const vehicleFactory = {
    createvehicle: function(type){
        switch(type.toLowerCase()){
            case "car":
                return new Car();
            case 'truck':
                return new Truck();
            case 'bike':
                return new Bike();
            default:
                return null
        }
    }
};

const car = vehicleFactory.createvehicle('Car');
const truck = vehicleFactory.createvehicle('Truck');
const bike = vehicleFactory.createvehicle('Bike');
const unkown = vehicleFactory.createvehicle('Boat');

console.log(car)
console.log(truck)
console.log(bike)
console.log(unkown)
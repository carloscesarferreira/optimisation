from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

unit_price = 2.50
month_business_days = 22
year_business_days = 253

def create_data_model():
    # Stores the data for the problem
    data = {}
    data['distance_matrix'] = [
        [000,	573,	950,	1235,	1540,	337,	360,	923,	713,	567,	413],
        [573,	000,	405,	716,	406,	570,	370,	960,	650,	513,	543],
        [950,	405,	000,	530,	340,	570,	750,	1433,	916,	826,	525],
        [1235,	716,	530,	000,	760,	1116,	1130,	1786,	1393,	1260,	1053],
        [1540,	406,	340,	760,	000,	356,	526,	1223,	876,	733,	305],
        [337,	570,	570,	1116,	356,	000,	360,	1080,	753,	643,	180],
        [360,	370,	750,	1130,	526,	360,	000,	653,	463,	463,	396],
        [923,	960,	1433,	1786,	1223,	1080,	653,	000,	365,	390,	1010],
        [713,	650,	916,	1393,	876,	753,	463,	365,	000,	126,	816],
        [567,	513,	826,	1260,	733,	643,	463,	390,	126,	000,	593],
        [413,	543,	525,	1053,	305,	180,	396,	1010,	816,	593,	000],
    ]
    data['demands'] = [0, 1, 1, 0.5, 0.7, 1, 0.5, 0.3, 2, 2, 1.9] #demands 
    data['vehicle_capacities'] = [12] # vehicle capacity
    data['num_vehicles'] = 1 # number of vehicles
    data['depot'] = 0 # set the DC
    return data


def print_solution(data, manager, routing, solution):
    # print solution on console
    total_distance = 0
    total_load = 0
    for vehicle_id in range(data['num_vehicles']):
        index = routing.Start(vehicle_id)
        plan_output = 'Route for vehicle {}:\n'.format(vehicle_id)
        route_distance = 0
        route_load = 0
        while not routing.IsEnd(index):
            node_index = manager.IndexToNode(index)
            route_load = data['demands'][node_index]
            plan_output += ' {0} Delivery({1}) -> '.format(node_index,route_load)
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_distance += routing.GetArcCostForVehicle(
                previous_index, index, vehicle_id)
        plan_output += ' {0} Delivery({1})\n'.format(manager.IndexToNode(index),
                                                 route_load)

        print(plan_output)
        total_distance += route_distance
        total_load += route_load
    print('Total distance of all routes: {0:.2f} km/day'.format(total_distance/100))
    print('Total distance of all routes: {0:.2f} km/month'.format((total_distance/100)*month_business_days))
    print('Total distance of all routes: {0:.2f} km/year \n'.format((total_distance/100)*year_business_days))    
    print('Total value of all routes: {0:.2f} Euros/day'.format((total_distance/100)*unit_price))
    print('Total value of all routes: {0:.2f} Euros/month'.format((total_distance/100)*unit_price*month_business_days))
    print('Total value of all routes: {0:.2f} Euros/year \n'.format((total_distance/100)*unit_price*year_business_days))    
    print('Routing Status: {0:.2f}\n'.format(routing.status()))

def main():

    # Instantiate the data problem.
    data = create_data_model()

    # Create the routing index manager.
    manager = pywrapcp.RoutingIndexManager(len(data['distance_matrix']), data['num_vehicles'], data['depot'])

    # Create Routing Model.
    routing = pywrapcp.RoutingModel(manager)


    # Create and register a transit callback.
    def distance_callback(from_index, to_index):
               # Convert from routing variable Index to distance matrix NodeIndex.
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return data['distance_matrix'][from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)

    # Define cost of each arc.
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)


    # Add Capacity constraint.
    def demand_callback(from_index):
                # Convert from routing variable Index to demands NodeIndex.
        from_node = manager.IndexToNode(from_index)
        return data['demands'][from_node]

    demand_callback_index = routing.RegisterUnaryTransitCallback(demand_callback)
    routing.AddDimensionWithVehicleCapacity(
        demand_callback_index,
        0,  # null capacity slack
        data['vehicle_capacities'],  # vehicle maximum capacities
        True,  # start cumul to zero
        'Capacity')

    # Setting first solution strategy and local search
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)
    search_parameters.local_search_metaheuristic = (routing_enums_pb2.LocalSearchMetaheuristic.GUIDED_LOCAL_SEARCH)
    search_parameters.time_limit.FromSeconds(1)

    # Solve the problem.
    solution = routing.SolveWithParameters(search_parameters)

    # Print solution on console.
    if solution:
        print_solution(data, manager, routing, solution)

if __name__ == '__main__':
    main()



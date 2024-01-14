import carla

# Connect to client
client = carla.Client('localhost', 2000)
client.set_timeout(10.0)

# Get current world
world = client.get_world()

# Tick world to get current data
world.tick()

# Get length of actor list
actor_list = world.get_actors()
actor_list_length = actor_list.__len__()

# Set all traffic lights to green
# Iterate through list number not id
for x in range(0,actor_list_length-1):
 actor = world.get_actor(actor_list[x].id)
 if actor.type_id == "traffic.traffic_light":
  actor.set_state(carla.TrafficLightState.Green)
  print("Traffic light with ID ", x, " at ", actor.get_location()," set to Green", sep="")

# Freeze traffic states
world.freeze_all_traffic_lights(True)
print("Traffic lights set permanently")
 
# Destroy speed limits of 90 or 60
for x in range(0, actor_list_length-1):
 actor = world.get_actor(actor_list[x].id)
 if actor.type_id == "traffic.speed_limit.90" or actor.type_id == "traffic.speed_limit.60":
  actor.destroy()
  print("Speed limit with id=", x, " destroyed")

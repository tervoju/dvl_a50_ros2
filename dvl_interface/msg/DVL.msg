#time_stamp
string time_stamp
#frame_id
string frame_id
#Time
float64 time
#Measured velocity [m/s]
geometry_msgs/Vector3 velocity
#Figure of Merit
float64 fom
#Altitude of the sensor
float64 altitude
#Beams/Transducers
DVLBeam[4] beams 
#Validity of velocity
bool velocity_valid
#Status message
int64 status
#Formatting of json
string form

# data-store
File based key-value data store.

NOTE:

  1)"store.json" is a file used to store data.If you want to create this file in particular path then follow the next step.
  2)During instantiation of class if path specified then the "store.json" file is stored in that path. 
   ----The path must be raw string.Because the path contain backslash(it is consider as String Literal){ex : dataStore(r"<path_for_store.json_file>") }---- 

function:


<--1--> [create function],
     Parameter => key ,value,time(optinal);
                  key   = Key name in which the value is store;
                  value = Json object(which is stored under the key) ;
                  time  = Integer(Time-to-live ,It is optinal.If specified ,then the key-value will be deleted after the given time)(In seconds);
     Return    => 1)if key is already in the data store, then "Key is already availabe in Data Store" is returned as response.;
                  2)if key is not in the data store,it will create a new key and add the value.Then ,return "Success, key-value pair are added to the Data Store" ;
    NOTE---> if time is specified then timeToKill function is invoked ;
             timeToKill will delete the key pair after specified time (with the help of deleteAfterExpire function);
             These process is done with the help of thread ;
<--2-->[read function],
    parameter =>  key;
                  key   = key to be searched in the Data Store;
    Return    =>  1)If key is not in the Data Store,then "Key is not in the Data Store" will be returned.;
                  2)If key is in the Data Store,then the Json Object(which is stored under the key) is returned as response.;
<--3-->[delete function],
    Parameter => key;
                 key   = key-value pair needed to deleted in the Data Store;
    Return    =>  1)If key is not in the Data Store,then "Key is not in the Data Store" will be returned.;
                  2)If key is in the Data Store,then key-pair is removed and "Key&pair is removed Successfully" is returned as response.;

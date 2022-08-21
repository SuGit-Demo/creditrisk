def checkLogin(user, pwd):
  #pip install ibm_db

  import ibm_db

  ###conn_str='database=pydev;hostname=host.test.com;port=portno;protocol=tcpip;uid=db2inst1;pwd=secret'
  #conn_str='database=bludb;hostname=98538591-7217-4024-b027-8baa776ffad1.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud;port=30875;protocol=TCPIP;uid=vjd81886;pwd=OicRrtEgVpnkIaxU'
  
  ############################
  dsn_hostname = "98538591-7217-4024-b027-8baa776ffad1.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud"# e.g.: "dashdb-txn-sbox-yp-dal09-04.services.dal.bluemix.net"
  dsn_uid = "vjd81886"# e.g. "abc12345"
  dsn_pwd = "OicRrtEgVpnkIaxU"# e.g. "7dBZ3wWt9XN6$o0J"
    
  dsn_driver = "{IBM DB2 ODBC DRIVER}"
  dsn_database = "bludb"            # e.g. "BLUDB"
  dsn_port = "30875"                # e.g. "50000" 
  dsn_protocol = "TCPIP"            # i.e. "TCPIP"
  dsn_security = "SSL"
    
  dsn = (
  "DRIVER={0};"
  "DATABASE={1};"
  "HOSTNAME={2};"
  "PORT={3};"
  "PROTOCOL={4};"
  "UID={5};"
  "PWD={6};"
  "SECURITY={7};").format(dsn_driver, dsn_database, dsn_hostname, dsn_port, dsn_protocol, dsn_uid, dsn_pwd, dsn_security)
    
  try:
    conn = ibm_db.connect(dsn, "", "")
    print ("Connected to database: ", dsn_database, "as user: ", dsn_uid, "on host: ", dsn_hostname)        

  except:
    print ("no connection:", ibm_db.conn_errormsg())

  #query_str = f"select * from VJD81886.CUSTOMER where COLUMN_0 = '{input_fruit}'"
  query_str = f"select * from VJD81886.CUSTOMER where Username = '{user}' and Password = '{pwd}'"
  selectQuery = query_str
    
  #Execute the statement
  selectStmt = ibm_db.exec_immediate(conn, selectQuery)
    
  #Fetch the Dictionary (for the first row only) - replace ... with your code
  output = ibm_db.fetch_tuple(selectStmt)

  if output:
    return 1
  else:
    return 0


sql_query = "SELECT TOP 1000 * FROM RegAllocDetailed_SCHEMA_A_TER_2022_01_01 WHERE 1 = 1 AND sheet_name = '0010'AND row_name = '1125'"
#sql_query = "Use GO SELECT contract_id FROM RegAllocDetailed_FINREP_BE_DP_5_1 WHERE lot_id = '956' AND BAS = 'Assets' AND PUR = 'Credit for Consumption'"
results = query_database(sql_query)
db.createUser(
{
	user: "database_2021",
	pwd: "qazwsx",
	roles: [
		{
			role: "readWrite",
			db: "data_integration"
		}
	]
}
)

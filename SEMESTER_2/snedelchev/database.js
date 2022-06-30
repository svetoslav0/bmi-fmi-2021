import { MongoClient } from "mongodb";

const mongoUri = "mongodb://localhost:27017"
const mongoClient = new MongoClient(mongoUri, {
    useNewUrlParser: true,
    useUnifiedTopology: true,
});

let dbConnection;

const connectToServer = (callback = () => {}) => {
    mongoClient.connect((error, database ) => {
        if (error || !database) {
            return callback(error);
        }

        dbConnection = database.db('kirc');
        console.log('Connected successfully to MongoDB database');

        return callback();
    });
};

const getDb = () => {
    return dbConnection;
}

export {
    connectToServer,
    getDb
};

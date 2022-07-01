import express from "express";

import { getDb } from "./database.js";
import { DataFormatBuilder } from "./helpers/DataFormatBuilder.js";

const router = express.Router();


router.post('/', (req, res) => {
    const databaseConnection = getDb();
    const data = DataFormatBuilder.formatAddData(req.body);

    databaseConnection
        .collection('clinical_data')
        .insertOne(data, (error, result) => {
            if (error) {
                console.error(error);
            }

            console.log(result);
            res.json({
                success: true
            });
        });
});

router.get('/', (req, res) => {
    const databaseConnection = getDb();

    const data = {};

    databaseConnection.collection('clinical_data')
        .insertOne(data, function(err, result) {
            if (err) {
                console.log(err)
            }

            console.log(result);
            res.send('Success!');
        });
});

export {
    router
};

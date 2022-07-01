import express from 'express';
import { ObjectId } from 'mongodb';

import { getDb } from './database.js';
import { removeUndefinedProps } from './helpers/utils.js';
import { ExposureFormatBuilder } from './helpers/ExposureFormatBuilder.js';
import { TreatmentsFormatBuilder } from './helpers/TreatmentsFormatBuilder.js';

const router = express.Router();

router.post('/exposures', (req, res) => {
    const data = ExposureFormatBuilder.formatCreateOrUpdate(req.body);

    getDb()
        .collection('exposures')
        .insertOne(data, (error, result) => {
            if (error) {
                console.error(error);
            }

            data.exposure_id = data._id.toString();
            const updated = { $set: data };
            getDb()
                .collection('exposures')
                .updateOne({ _id: new ObjectId(data.exposure_id) }, updated, err => {
                if (err) {
                    console.error(err);
                }

                return res
                    .status(201)
                    .json({ insertedId: result.insertedId });
            });
        });
});

router.get('/exposures/:id', (req, res) => {
    const id = req.params.id;

    getDb()
        .collection('exposures')
        .findOne({ _id: new ObjectId(id) }, (err, result) => {
            if (err) {
                console.error(err);
            }

            if (!result) {
                return res.status(404).json({ message: 'Not found' });
            }

            res.json(result);
        });
});

router.get('/exposures', (req, res) => {
    const limit = +req.query.limit || 10;
    const offset = +req.query.offset || 0;

    getDb()
        .collection('exposures')
        .find()
        .limit(limit)
        .skip(offset)
        .toArray((err, result) => {
            if (err) {
                console.log(err);
            }

            res.json(result);
        });
});

router.patch('/exposures/:id', (req, res) => {
    const id = req.params.id;
    const data = ExposureFormatBuilder.formatCreateOrUpdate(req.body);
    removeUndefinedProps(data);

    getDb()
        .collection('exposures')
        .findOne({ _id: new ObjectId(id) }, (err, result) => {
            if (err) {
                console.error(err);
            }

            if (!result) {
                return res.status(404).json({ message: 'Not found' });
            }

            const updated = {
                $set: { ...result, ...data }
            };

            getDb()
                .collection('exposures')
                .updateOne({ _id: new ObjectId(result._id) }, updated, err => {
                    if (err) {
                        console.error(err);
                    }

                    res.status(204).json();
                });
        });
});

router.delete('/exposures/:id', (req, res) => {
    const id = req.params.id;

    getDb()
        .collection('exposures')
        .findOne({ _id: new ObjectId(id) }, (err, result) => {
            if (err) {
                console.error(err);
            }

            if (!result) {
                return res.status(404).json({ message: 'Not found' });
            }

            getDb()
                .collection('exposures')
                .deleteOne({ _id: new ObjectId(id) }, (err, result) => {
                    if (err) {
                        console.log(err);
                    }

                    res.status(204).json();
                })
        });
});

router.post('/treatments', (req, res) => {
    const data = TreatmentsFormatBuilder.formatCreateOrUpdate(req.body);

    getDb()
        .collection('treatments')
        .insertOne(data, (error, result) => {
            if (error) {
                console.error(error);
            }

            data.treatment_id = data._id.toString();
            const updated = { $set: data };

            getDb()
                .collection('treatments')
                .updateOne({ _id: new ObjectId(data.treatment_id) }, updated, err => {
                    if (err) {
                        console.error(err);
                    }

                    return res
                        .status(201)
                        .json({ insertedId: result.insertedId });
                });
        });
});

export {
    router
};

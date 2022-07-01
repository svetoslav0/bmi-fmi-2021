import fs from 'fs';

import { connectToServer, getDb } from '../../database.js';

const data = JSON.parse(fs.readFileSync('initial_data.json', 'utf8'));

connectToServer(error => {
    if (error) {
        console.error(error);
        process.exit(1);
    }

    const databaseConnection = getDb();

    data.forEach(caseObj => {
        const exposures = caseObj.exposures;
        exposures.forEach(e => {

            const exposureId = e.exposure_id;

            databaseConnection
                .collection('exposures')
                .findOne({ exposure_id: exposureId }, (err, result) => {
                    if (err) {
                        console.log(err)
                    }

                    if (!result) {
                        databaseConnection
                            .collection('exposures')
                            .insertOne(e, (err, res) => {
                                if (err) {
                                    console.log(err);
                                }
                            });
                    } else {
                        console.log(`Skipping E with ID ${exposureId}`);
                    }
                });
        });

        const diagnoses = caseObj.diagnoses;
        diagnoses.forEach(d => {
            const treatments = d.treatments;
            treatments.forEach(t => {
                const treatmentId = t.treatment_id;

                databaseConnection
                    .collection('treatments')
                    .findOne({ treatment_id: treatmentId }, (err, result) => {
                        if (err) {
                            console.log(err);
                        }

                        if (!result) {
                            databaseConnection
                                .collection('treatments')
                                .insertOne(t, (err, res) => {
                                    if (err) {
                                        console.log(err);
                                    }
                                });
                        } else {
                            console.log(`Skipping T with ID ${treatmentId}`);
                        }
                    });
            });

            const treatmentIds = d.treatments.map(t => t.treatment_id);

            delete d.treatments;
            d.treatments = treatmentIds;

            databaseConnection
                .collection('diagnoses')
                .insertOne(d, (err, res) => {
                    if (err) {
                        console.log(err)
                    }
                });
        });

        const exposureIds = caseObj.exposures.map(e => e.exposure_id);
        const diagnoseIds = caseObj.diagnoses.map(d => d.diagnosis_id);

        delete caseObj.exposures;
        delete caseObj.diagnoses;

        caseObj.exposures = exposureIds;
        caseObj.diagnoses = diagnoseIds;

        databaseConnection
            .collection('clinical_cases')
            .insertOne(caseObj, (err, res) => {
                if (err) {
                    console.log(err);
                }
            });
    });

    console.log('Done.')
});

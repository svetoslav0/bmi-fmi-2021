import express from "express";

const router = express.Router();

import { getDb } from "./database.js";

router.get('/', (req, res) => {
    const databaseConnection = getDb();

    const data = {
        "exposures": [
            {
                "cigarettes_per_day": null,
                "alcohol_history": "Not Reported",
                "updated_datetime": "2019-07-31T23:03:56.418889-05:00",
                "exposure_id": "ad752a20-c397-5d9c-bfa3-e8077fbda185",
                "submitter_id": "TCGA-CW-5584_exposure",
                "years_smoked": null,
                "state": "released",
                "created_datetime": null,
                "alcohol_intensity": null
            }
        ],
        "case_id": "09c4ea05-928d-49b7-b7fb-30cff3481b14",
        "diagnoses": [
            {
                "synchronous_malignancy": "No",
                "ajcc_pathologic_stage": "Stage III",
                "days_to_diagnosis": 0,
                "created_datetime": null,
                "treatments": [
                    {
                        "days_to_treatment_end": null,
                        "days_to_treatment_start": null,
                        "treatment_id": "2a78c0dd-133a-562d-b09b-66e4a19c762c",
                        "submitter_id": "TCGA-CW-5584_treatment_1",
                        "treatment_type": "Pharmaceutical Therapy, NOS",
                        "regimen_or_line_of_therapy": null,
                        "treatment_effect": null,
                        "therapeutic_agents": null,
                        "treatment_or_therapy": "no",
                        "created_datetime": "2019-04-28T14:57:54.610714-05:00",
                        "initial_disease_status": null,
                        "treatment_intent_type": null,
                        "treatment_anatomic_site": null,
                        "updated_datetime": "2019-07-31T23:03:56.418889-05:00",
                        "treatment_outcome": null,
                        "state": "released"
                    },
                    {
                        "treatment_intent_type": null,
                        "updated_datetime": "2019-07-31T23:03:56.418889-05:00",
                        "treatment_id": "809b7268-0256-5951-82f6-1fa65d525b73",
                        "submitter_id": "TCGA-CW-5584_treatment",
                        "treatment_type": "Radiation Therapy, NOS",
                        "state": "released",
                        "therapeutic_agents": null,
                        "treatment_or_therapy": "no",
                        "created_datetime": null
                    }
                ],
                "last_known_disease_status": "not reported",
                "tissue_or_organ_of_origin": "Kidney, NOS",
                "days_to_last_follow_up": null,
                "age_at_diagnosis": 27352,
                "primary_diagnosis": "Clear cell adenocarcinoma, NOS",
                "updated_datetime": "2019-08-08T16:53:29.535496-05:00",
                "prior_malignancy": "no",
                "year_of_diagnosis": 2003,
                "state": "released",
                "prior_treatment": "No",
                "days_to_last_known_disease_status": null,
                "ajcc_pathologic_t": "T3b",
                "days_to_recurrence": null,
                "morphology": "8310/3",
                "ajcc_pathologic_n": "N1",
                "ajcc_pathologic_m": "M0",
                "submitter_id": "TCGA-CW-5584_diagnosis",
                "classification_of_tumor": "not reported",
                "diagnosis_id": "1a5e3656-9735-5c7a-8436-245aa16af975",
                "icd_10_code": "C64.9",
                "site_of_resection_or_biopsy": "Kidney, NOS",
                "tumor_grade": "not reported",
                "progression_or_recurrence": "not reported"
            }
        ],
        "demographic": {
            "race": "white",
            "gender": "male",
            "ethnicity": "not hispanic or latino",
            "vital_status": "Dead",
            "age_at_index": 74,
            "submitter_id": "TCGA-CW-5584_demographic",
            "days_to_birth": -27352,
            "created_datetime": null,
            "year_of_birth": 1929,
            "demographic_id": "cf5ca056-a43e-5e63-88e0-0347139b32be",
            "updated_datetime": "2019-07-31T23:03:56.418889-05:00",
            "days_to_death": 164,
            "state": "released",
            "year_of_death": 2003
        }
    };

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

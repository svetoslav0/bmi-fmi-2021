import express from 'express';
import axios from 'axios';
import fasta from 'fasta-parser';

import { APISpecification } from './APISpecification.js';

const router = express.Router();

router.get('/specification', (req, res) => {
    const specification = APISpecification();

    return res.send(specification);
});

router.get('/gene/:id/sequence', async (req, res) => {
    const id = req.params.id; // ENSG00000157764

    const seqResult = await axios.get(`https://rest.ensembl.org/sequence/id/${id}`);
    const { seq } = seqResult.data;

    const exonsResult = (await axios.get(`https://rest.ensembl.org/lookup/id/${id}?expand=1`))
        .data
        .Transcript[0]
        .Exon;

    const exons = exonsResult.map(e => {
        return {
            start: e.start,
            end: e.end,
            id: e.id
        };
    });

    return res.send({
        seq,
        exons
    });
});

router.get('/sequence/:id/?content-type=fasta', async (req, res) => {
    const id = req.params.id;

    const fastaResult = await axios.get(`https://rest.ensembl.org/sequence/id/${id}?content-type=text/x-fasta`);
    console.log(fastaResult);

    return res.send('test');
});

export { router };

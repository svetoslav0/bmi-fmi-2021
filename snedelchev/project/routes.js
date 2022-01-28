import express from 'express';
import axios from 'axios';

const router = express.Router();

router.get('/sequence/gene/:id', async (req, res) => {
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

    res.send({
        seq,
        exons
    });
});

export { router };

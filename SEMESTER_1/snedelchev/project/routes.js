import express from 'express';
import axios from 'axios';
import parser from 'bio-parsers';

import { ApiError } from './ApiError.js';
import { ApiSpecification } from './ApiSpecification.js';
import {GC, getBasesFromSwapParam, getSequence, swapBases} from './utils.js';

const router = express.Router();

router.get('/specification', (req, res) => {
    const specification = ApiSpecification();

    return res.send(specification);
});

router.get('/gene/:id/sequence', async (req, res) => {
    const id = req.params.id; // ENSG00000157764

    let seq = null;
    try {
        seq = await getSequence(id);
    } catch (e) {
        return res
            .status(400)
            .send({
                message: e.message
            });
    }

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

router.get('/sequence/:id/gc_content', async (req, res) => {
    const id = req.params.id; // &swap=A:T

    let seq = null;
    try {
        seq = await getSequence(id);
    } catch (e) {
        return res
            .status(400)
            .send({
                message: e.message
            });
    }

    let swap_seq = seq;

    try {
        const [swapBaseOne, swapBaseTwo] = getBasesFromSwapParam(req.query.swap);

        if (swapBaseOne && swapBaseTwo) {
            swap_seq = swapBases(seq, swapBaseOne, swapBaseTwo);
        }
    } catch (e) {
        if (e instanceof ApiError) {
            return res
                .status(400)
                .send({
                    message: e.message
                });
        }

        throw e;
    }

    return res.send({
        seq,
        gc_content: GC(seq),
        swap_seq
    });
});

router.get('/sequence/:id', async (req, res) => {
    const id = req.params.id;

    const data = await axios.get(`https://rest.ensembl.org/sequence/id/${id}?content-type=text/x-fasta`);
    const fasta = parser.fastaToJson(data.data);

    const result = fasta.map(f => {
        return {
            id: f.parsedSequence.name,
            seq: f.parsedSequence.sequence
        };
    });

    return res.send(result);
});

export { router };

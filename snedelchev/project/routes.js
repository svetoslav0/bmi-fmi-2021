import express from 'express';

const router = express.Router();

router.get('/', (req, res) => {
    const result = {
        message: 'success!'
    };

    res.json(result);
});

export { router };

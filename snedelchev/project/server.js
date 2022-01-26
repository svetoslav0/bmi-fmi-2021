import express from 'express';
import morgan from 'morgan';

import { router } from './routes.js';

const app = express();
const port = 9091; // todo: move in config

app.use(morgan('dev'));

app.use(router);

// todo: add express exception handler

app.listen(port, () => console.log(`Running on port ${port} . . .`));

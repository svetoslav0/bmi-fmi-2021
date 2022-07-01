import express from "express";
import cors from "cors";
import bodyParser from "body-parser";

import { connectToServer } from "./database.js";
import { router } from "./router.js";

const POST = 4041;
const app = express();

app.use(cors());
app.use(bodyParser.urlencoded({ extender: false }));
app.use(bodyParser.json());
app.use(express.json());
app.use(router);

connectToServer(error => {
    if (error) {
        console.error(error);
        process.exit(1);
    }

    app.listen(POST, () => { console.log(`Listening on port ${POST} . . .`) })
});

import express from "express";
import cors from "cors";

import { connectToServer } from "./database.js";
import { router } from "./router.js";

const POST = 4041;
const app = express();

app.use(cors());
app.use(express.json());
app.use(router);

connectToServer(error => {
    if (error) {
        console.error(error);
        process.exit();
    }

    app.listen(POST, () => { console.log(`Listening on port ${POST} . . .`) })
});

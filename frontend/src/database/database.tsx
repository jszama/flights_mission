const db = require("mongoose");
const uri = process.env.MONGODB_URI;

export async function connectToDatabase() {
    try {
        db.connect(uri);
        console.log("Connected to MongoDB");
    } catch (error) {
        console.error("Failed to connect to MongoDB", error);
        process.exit(1);
    }
  }
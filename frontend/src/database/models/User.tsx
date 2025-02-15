import mongoose, { Schema } from 'mongoose';

const UserSchema: Schema = new Schema({
    email: { type: String, required: true, unique: true },
    firstName: { type: String, required: true },
    lastName: { type: String, required: true },
    password: { type: String, required: true },
});

export interface IUser extends mongoose.Document {
    _id: Schema.Types.ObjectId;
    email: string;
    firstName: string;
    lastName: string;
    password: string;
}

export const User = mongoose.models.User || mongoose.model('User', UserSchema);

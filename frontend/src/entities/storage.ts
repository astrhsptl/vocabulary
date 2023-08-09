import  { configureStore, combineReducers } from "@reduxjs/toolkit";
import townSlice from "./toolkitSlices";


const rootReducer = combineReducers({
    toolkit: townSlice
});

export const store = configureStore({
    reducer: rootReducer,
})
import { createSlice, PayloadAction } from "@reduxjs/toolkit";
    
const townSlice = createSlice({
    name: 'word',
    initialState: {
        town: {},
    },
    
    reducers: {
    }
});

export default townSlice.reducer
export const {setCurrentTown} = townSlice.actions;
import { ApiError } from './ApiError.js';

/**
 * @param {string} sequence
 * @returns {number}
 */
export const GC = sequence => {
    sequence = sequence.toUpperCase();

    const gcLength = (sequence.match(/G/g) || []).length + (sequence.match(/C/g) || []).length;
    const length = sequence.length;

    return Math.round(gcLength / length * 100);
};

/**
 * @param {string} swapParam
 * @returns {string[]}
 */
export const getBasesFromSwapParam = swapParam => {
    if (!swapParam) {
        return [null, null];
    }

    const regex = /^\w:\w$/g;
    const match = swapParam.match(regex);

    if (!match) {
        throw new ApiError('Incorrect format of swap param. Must provide two bases separated by colon. Example: A:T');
    }

    return swapParam.split(':') ?? [null, null];
};

export const swapBases = (seq, swapBaseOne, swapBaseTwo) => { // A, C
    seq = seq.toLowerCase(); // ATCGTA -> CTAGTC

    return seq.split(swapBaseOne.toLowerCase())
        .join(swapBaseTwo.toUpperCase())
        .split(swapBaseTwo.toLowerCase())
        .join(swapBaseOne.toUpperCase())
        .toUpperCase();
};

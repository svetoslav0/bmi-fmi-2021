const APPLICATION_VERSION = '1.0.0';
const DEV_CONTACT_EMAIL = 'svet.nedelchev@gmail.com';
const APPLICATION_HOST = 'localhost:9091'; // TODO: get the host from config

export const ApiSpecification = () => {
    return {
        swagger: '2.0',
        info: {
            description: 'RESTful API // TODO',
            version: APPLICATION_VERSION,
            title: 'TODO',
            contact: {
                email: DEV_CONTACT_EMAIL
            }
        },
        host: APPLICATION_HOST,
        tags: [
            {
                name: 'Gene',
                description: 'Gene Related Paths'
            }
        ],
        paths: {
            '/gene/{id}/sequence': {
                get: {
                    tags: [
                        'Gene',
                        'Sequence'
                    ],
                    summary: 'Get gene sequence',
                    description: 'Get gene sequence and list of exons by provided ID.',
                    operationId: 'getGeneSequence',
                    parameters: [
                        {
                            name: 'id',
                            in: 'path',
                            description: 'The ID of the gene',
                            required: true,
                            type: 'string'
                        }
                    ],
                    responses: {
                        200: {
                            description: 'Gene data with exons',
                            schema: {
                                $ref: '#/definitions/GeneData'
                            }
                        },
                        400: {
                            description: 'Bad Request',
                            schema: {
                                $ref: '#/definitions/BadRequest'
                            }
                        }
                    }
                }
            },
            '/sequence/{id}/gc_content': {
                get: {
                    tags: [
                        'Sequence'
                    ],
                    summary: 'Get GC content and swapped bases',
                    description: 'This method returns GC content (percentage content of G and C bases in the sequence) and swaps two bases by provided bases in the swap parameter',
                    operationId: 'getGcContentData',
                    parameters: [
                        {
                            name: 'id',
                            in: 'path',
                            description: 'The ID of the gene',
                            required: true,
                            type: 'string'
                        },
                        {
                            name: 'swap',
                            in: 'query',
                            description: 'Swap parameter. Pass the two bases that need to be swapped in the following format: {base-one}:{base-two}. Examples: A:T, G:C, A:C',
                            required: false,
                            type: 'string'
                        }
                    ],
                    responses: {
                        200: {
                            description: 'GC content data',
                            schema: {
                                $ref: '#/definitions/GCData'
                            }
                        },
                        400: {
                            description: 'Bad Request',
                            schema: {
                                $ref: '#/definitions/BadRequest'
                            }
                        }
                    }
                }
            },
            '/sequence/{id}': {
                get: {
                    tags: [
                        'Sequence'
                    ],
                    summary: 'Sequence data',
                    description: 'Returns sequence and it\'s ID',
                    operationId: 'getSequenceData',
                    parameters: [
                        {
                            name: 'id',
                            in: 'path',
                            description: 'The ID of the gene',
                            required: true,
                            type: 'string'
                        }
                    ],
                    responses: {
                        200: {
                            description: 'Sequences data',
                            schema: {
                                $ref: '#/definitions/SequencesData'
                            }
                        },
                        400: {
                            description: 'Bad Request',
                            schema: {
                                $ref: '#/definitions/BadRequest'
                            }
                        }
                    }
                }
            }
        },
        definitions: {
            GeneData: {
                type: 'object',
                properties: {
                    seq: {
                        type: 'string',
                        description: 'The sequence'
                    },
                    exons: {
                        type: 'array',
                        description: 'List of gene exons',
                        items: {
                            $ref: '#/definitions/Exon'
                        }
                    }
                }
            },
            Exon: {
                type: 'object',
                properties: {
                    start: {
                        type: 'integer',
                        description: 'Exon start'
                    },
                    end: {
                        type: 'integer',
                        description: 'Exon end'
                    },
                    id: {
                        type: 'string',
                        description: 'Exon ID'
                    }
                }
            },
            GCData: {
                type: 'object',
                description: 'GC and swapped data',
                properties: {
                    seq: {
                        type: 'string',
                        description: 'The sequence by the provided ID'
                    },
                    gc_content: {
                        type: 'integer',
                        description: 'Percentage of G and C bases'
                    },
                    swap_seq: {
                        type: 'string',
                        description: 'Swapped sequence by given swap bases. If swap parameter is not provided, the value must be the same as the seq field'
                    }
                }
            },
            SequencesData: {
                type: 'array',
                description: 'List of sequences',
                items: {
                    $ref: '#/definitions/SequenceData'
                }
            },
            SequenceData: {
                type: 'object',
                properties: {
                    id: {
                        type: 'string',
                        description: 'Sequence ID with it\'s metadata'
                    },
                    seq: {
                        type: 'string',
                        description: 'The sequence itself'
                    }
                }
            },
            BadRequest: {
                type: 'object',
                properties: {
                    message: {
                        type: 'string',
                        description: 'Message with description of the issue'
                    }
                }
            }
        }
    };
}

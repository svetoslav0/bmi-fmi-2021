const APPLICATION_VERSION = '1.0.0';
const CONTACT_EMAIL = 'svet.nedelchev@gmail.com';
const APPLICATION_HOST = 'localhost:9091'; // TODO: get the host from config

export const APISpecification = () => {
    return {
        swagger: '2.0',
        info: {
            description: 'RESTful API // TODO',
            version: APPLICATION_VERSION,
            title: 'TODO',
            contact: {
                email: CONTACT_EMAIL
            }
        },
        host: APPLICATION_HOST,
        tags: [
            {
                name: 'Gene',
                description: 'Gene Related Paths'
            },
            {
                name: 'Sequence',
                description: 'Sequence Related Paths'
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
                        } // TODO: Add 400 response schema
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
                        } // TODO: Add 400 response schema
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
            }
        }
    };
}

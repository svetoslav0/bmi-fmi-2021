import chai from 'chai';
import chaiHttp from 'chai-http';

import server from './server.js';

const should = chai.should();
chai.use(chaiHttp)

const existingIdOne = 'ENSG00000157764';
const existingIdTwo = '123';
const nonExistingId = 'qweasdqwe123';

const swapParam = 'A:T';

const expectedNameOfIdOne = 'ENSG00000157764.14 chromosome:GRCh38:7:140719327:140924929:-1';

const seqForIdTwo = 'TTGGAGAAGCTCATTTATTACCCGGCCTTTAAATCCACCCTGAACCAGGTGACCGGCAAGTACCAGTTAAATCCACAGATGCTCTGCCAGTGGAAGAGCGACTTTATCAAGAATGCCGCTATGGTCTTCGAACATAACAAGGACGAGGCCGGGAAACTCAGGAAAGAGATGGAGGAAAAAGAATCCCGTTATCAACAGATCATTGGTCAGCAATCCTATGAGATTGACTGGCTCAAAAAAAACTGGCCTCAAGTAGTACGGTCGAAGTACGCAAAGCCATGGCGGAGCCTGGCAAACATCAAATCAGCCTTGCCCGGCAGGCCTTCAGCTGAGCGTTAA';
const expectedSwappedAAndTBases = 'AAGGTGTTGCACTAAATAATCCCGGCCAAATTTACCTCCCAGTTCCTGGAGTCCGGCTTGATCCTGAATTTACCTCTGTAGCACAGCCTGAGGTTGTGCGTCAAATACTTGTTAGCCGCATAGGACAACGTTCTATTCTTGGTCGTGGCCGGGTTTCACTGGTTTGTGTAGGTGGTTTTTGTTACCCGAATACTTCTGTACTAAGGACTGCTTACCATAGTGTAAGTCAGGCACTTTTTTTTCAGGCCACTTGATGATCGGACGTTGATCGCTTTGCCTAGGCGGTGCCAGGCTTTCTACTTTACTGCCAAGCCCGGCTGGCCAACTGCAGTGCGAATT';

describe('Sequence tests',() => {
    describe('GET /gene/:id/sequence tests', () => {
        it('Should test GET /gene/:id/sequence with success status', done => {
            chai.request(server)
                .get(`/gene/${existingIdOne}/sequence`)
                .end((err, result) => {
                    result.should.have.status(200);

                    result.body.should.have.property('seq');
                    result.body.should.have.property('exons');

                    result.body.seq.should.be.a('string');
                    result.body.exons.should.be.a('array');

                    result.body.exons.length.should.have.above(0);

                    result.body.exons[0].should.have.property('id');
                    result.body.exons[0].should.have.property('start');
                    result.body.exons[0].should.have.property('end');

                    result.body.exons[0].id.should.be.a('string');
                    result.body.exons[0].start.should.be.a('number');
                    result.body.exons[0].end.should.be.a('number');

                    done();
                });
        })
        .timeout(10000);

        it('Should test GET /gene/:id/sequence with non-success status', done => {
            chai.request(server)
                .get(`/gene/${nonExistingId}/sequence`)
                .end((err, result) => {
                    result.should.have.status(400);

                    result.body.should.have.property('message');

                    result.body.message.should.be.a('string');

                    done();
                });
        })
        .timeout(10000);

    });

    describe('GET /sequence/:id/gc_content tests', () => {
        it('Should test GET /sequence/:id/gc_content without swap param and should get success status', done => {
            chai.request(server)
                .get(`/sequence/${existingIdOne}/gc_content`)
                .end((err, result) => {
                    result.should.have.status(200);

                    result.body.should.have.property('seq');
                    result.body.should.have.property('gc_content');
                    result.body.should.have.property('swap_seq');

                    result.body.seq.should.equals(result.body.swap_seq);

                    done();
                });
        })
        .timeout(10000);


        it('Should test GET /sequence/:id/gc_content with swap param and should get success status', done => {
            chai.request(server)
                .get(`/sequence/${existingIdTwo}/gc_content?swap=${swapParam}`)
                .end((err, result) => {
                    result.should.have.status(200);

                    result.body.should.have.property('seq');
                    result.body.should.have.property('gc_content');
                    result.body.should.have.property('swap_seq');

                    result.body.seq.should.equals(seqForIdTwo);
                    result.body.swap_seq.should.equals(expectedSwappedAAndTBases);

                    done();
                });
        })
        .timeout(10000);

    });

    describe('GET /sequence/:id tests', () => {
        it('Should test GET /sequence/:id and get a success status', done => {
            chai.request(server)
                .get(`/sequence/${existingIdOne}`)
                .end((err, result) => {
                    result.should.have.status(200);

                    result.body.should.be.a('array');
                    result.body.length.should.have.above(0);

                    result.body[0].should.have.property('id');
                    result.body[0].should.have.property('seq');

                    result.body[0].id.should.equals(expectedNameOfIdOne);
                    result.body[0].seq.should.be.a('string');

                    done();
                });
        })
        .timeout(10000);

    });
});

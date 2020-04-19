#! /bin/bash

BASEDIR=$(pwd)/blog/language
SCRIPTS=$BASEDIR/mosesdecoder/scripts
TOKENIZER=$SCRIPTS/tokenizer/tokenizer.perl
CLEAN=$SCRIPTS/training/clean-corpus-n.perl
NORM_PUNC=$SCRIPTS/tokenizer/normalize-punctuation.perl
REM_NON_PRINT_CHAR=$SCRIPTS/tokenizer/remove-non-printing-char.perl
BPEROOT=$BASEDIR/subword-nmt/subword_nmt
BPE_TOKENS=40000
src=en
tgt=fr
tokenized_out=$(echo $1 | \
            perl $NORM_PUNC $src | \
            perl $REM_NON_PRINT_CHAR | \
            perl $TOKENIZER -threads 8 -a -l $src) #> temp_tokenized.out         
prep=$BASEDIR/wmt14.v2.en-fr.fconv-py
BPE_CODE=$prep/bpecodes
final_result=$(echo $tokenized_out | python $BPEROOT/apply_bpe.py -c $BPE_CODE)

MODEL_DIR=$BASEDIR/wmt14.v2.en-fr.fconv-py
echo $final_result | fairseq-interactive \
    --path $MODEL_DIR/model.pt $MODEL_DIR \
    --beam 1 --source-lang en --target-lang fr | grep "H-0" | cut -f3- | sed -r 's/(@-@ )|(@-@ ?$)//g' | sed -r 's/(@@ )|(@@ ?$)//g' 


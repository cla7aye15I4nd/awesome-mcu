#include "ai_datatypes_defines.h"
#include "ai_platform.h"
#include "mnist.h"
#include "mnist_data.h"

AI_ALIGNED(4) 
static ai_u8 activations[AI_MNIST_DATA_ACTIVATIONS_SIZE];
static ai_handle mnist_model = AI_HANDLE_NULL;

void model_init(void) {
    ai_mnist_create(&mnist_model, AI_MNIST_DATA_CONFIG);
    
    const ai_network_params ai_params = AI_NETWORK_PARAMS_INIT(
        AI_MNIST_DATA_WEIGHTS(ai_mnist_data_weights_get()),
        AI_MNIST_DATA_ACTIVATIONS(activations)
    );

    ai_mnist_init(mnist_model, &ai_params);
}

void model_run(void* in_data, void* out_data) {
    ai_buffer ai_input[AI_MNIST_IN_NUM] = AI_MNIST_IN;
    ai_buffer ai_output[AI_MNIST_OUT_NUM] = AI_MNIST_OUT;

    ai_input[0].n_batches = 1;
    ai_input[0].data = AI_HANDLE_PTR(in_data);
    ai_output[0].n_batches = 1;
    ai_output[0].data = AI_HANDLE_PTR(out_data);

    ai_mnist_run(mnist_model, &ai_input[0], &ai_output[0]);
}
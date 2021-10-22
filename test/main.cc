#include <node_embedding_api.h>
#include <vector>

int main(int argc, char** argv) {
	void* handle = node_prepare();
	node_run(handle);
	node_cleanup(handle);
}

#include <node.h>

extern "C" int node_start(int argc, char** argv) {
    return node::Start(argc, argv);
}

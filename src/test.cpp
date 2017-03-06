#include <iostream>
#include <iostream>
#include <annoylib.h>
#include <kissrandom.h>



using namespace std;

int main(int argc, char *argv[])
{
    AnnoyIndexInterface<int, float> *annoy_index = new AnnoyIndex<int, float, Angular, Kiss64Random>(20);

    float items[] = {1,2,3,1,1,1,1,1,1,4,5,12, 13};
    annoy_index->add_item(9999175, items);

    auto i = annoy_index->get_n_items();



    cout << "hello i="<<i<<endl; 
}
